# -*- encoding: utf-8 -*-
import struct

from binascii import hexlify
from socket import gethostname
from socketserver import BaseRequestHandler, TCPServer
from PyCRC.CRC16 import CRC16

DEFAULT_PACKET_LEN = 23


def first_match_from_buf(buffer: bytes) -> bytes:
    try:
        start = buffer.index(b'\xAA\x55')
    except ValueError:
        return b''
    pkt = bytes(buffer)
    while True:
        try:
            end = pkt.rindex(b'\x0D\x0A')
        except ValueError:
            # 前面找到了AA55, 但后面找不到0D0A
            if len(pkt) - start >= DEFAULT_PACKET_LEN:
                # 对于只有55AA没有0D0A的无效包, 丢弃2字节55AA以及55AA前面的无效内容, 保留原始 buffer 尾部内容
                return buffer[start + 2:]
            # 对于长度小于23的不完整包, 保留55AA, 只丢弃55AA前面的无效内容
            return buffer[start:]
        pkt_size = end + 2 - start
        if pkt_size == DEFAULT_PACKET_LEN:  # 数据包格式正确
            break
        pkt = pkt[:end]  # 继续从后往前寻找倒数第二个0D0A
    return pkt


class MyTCPHandler(BaseRequestHandler):
    debug = True
    debug_send_back = False

    def handle(self):

        crc16calc = CRC16(modbus_flag=True)
        recv_buf = bytearray(DEFAULT_PACKET_LEN)

        n = 0
        while True:
            view = memoryview(recv_buf)[n:]
            while n < DEFAULT_PACKET_LEN:
                tmp = self.request.recv_into(view)
                if tmp <= 0:
                    print('Warning: Client has shutdown the connection!')
                    return
                n += tmp
                view = view[tmp:]

            pkt = first_match_from_buf(recv_buf)
            n = len(pkt)
            if 0 == n:
                continue
            if 0 < n < DEFAULT_PACKET_LEN:
                recv_buf[:n] = pkt  # 数据包不完整(有头无尾), 需将包头回写进收缓冲区
                continue
            n = 0 if DEFAULT_PACKET_LEN == n else n - DEFAULT_PACKET_LEN
            # # TODO: 假如遇到超长的数据包,需要将超长部分回写进收缓冲区
            # if n > len(recv_buf):  # This should NEVER happen!
            #     n = 0
            #     continue
            # elif 0 < n <= DEFAULT_PACKET_LEN:
            #     recv_buf[:n] = pkt[DEFAULT_PACKET_LEN:DEFAULT_PACKET_LEN + n]

            # 拆包
            src_dev_addr, cmd, cnt, raw_data, crc_checksum = \
                struct.unpack('>HbH12sH', pkt[2:DEFAULT_PACKET_LEN - 2])  # 不需要解析起始/终止符

            # 计算并对比 CRC16 校验和是否一致
            crc = crc16calc.calculate(pkt[:DEFAULT_PACKET_LEN - 4])
            if crc != crc_checksum:
                print('Checksum error:',
                      'Received {:04X},'.format(crc_checksum),
                      'but should be {:04X}.'.format(crc)
                      )
                continue

            if self.debug:
                # 调试信息
                client_ip_addr, client_port = self.request.getpeername()
                print('Client ip={}, port={}, device_id={:04X}'.format(client_ip_addr, client_port, src_dev_addr))
                hex_str = hexlify(pkt).decode('ascii').upper()
                formatted_str = ' '.join([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)])  # 添加空格便于阅读
                print(formatted_str)
            if self.debug_send_back:
                # Just send back the same data
                self.request.sendall(pkt)


def main():
    host_addr = '0.0.0.0'
    port = 9999

    server = TCPServer((host_addr, port), MyTCPHandler)

    # TODO: 后台线程执行TCP端口监听
    # from threading import Thread
    # server_thread = Thread(target=server.serve_forever)
    # server_thread.daemon = True

    if '0.0.0.0' == host_addr:
        host_addr = gethostname()

    with server:
        print('Server infomation: hostname={} port={}'.format(host_addr, port))
        server.serve_forever()
    print('Main thread will exit now.')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ctrl_c:
        print('Info: Ctrl-C is pressed')
    print('Quiting...')
