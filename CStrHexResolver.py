import re

def decode_hex_gbk(text: str) -> str:
    # 匹配 \xXX 或者普通文本
    pattern = re.compile(r'(\\x[0-9a-fA-F]{2})|([^\\]+)')
    parts = pattern.findall(text)
    
    byte_buf = b""
    output = ""
    
    for hex_part, plain_part in parts:
        if hex_part:
            # 提取两位十六进制
            h = hex_part[2:]
            byte_buf += bytes([int(h, 16)])
        else:
            # 遇到普通文本，先把缓冲区的字节用GBK解码，再追加普通文本
            if byte_buf:
                try:
                    output += byte_buf.decode("gbk")
                except:
                    # GBK解码失败，还原成\xxx字符串
                    output += "".join(f"\\x{b:02x}" for b in byte_buf)
                byte_buf = b""
            output += plain_part
    # 处理剩下缓冲区里的字节
    if byte_buf:
        try:
            output += byte_buf.decode("gbk")
        except:
            output += "".join(f"\\x{b:02x}" for b in byte_buf)
    return output


if __name__ == "__main__":
    print("x码串:",end="")
    data = input().strip()
    out = decode_hex_gbk(data)
    print(f"{out}")
    import os
    os.system("pause")
