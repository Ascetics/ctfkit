"""SM4 对称加密演示（基于 gmssl 库）。

SM4 是中国商用密码标准（GB/T 32907-2016）的分组密码：
- 分组长度 128 bit（16 字节）
- 密钥长度 128 bit（16 字节）
- 32 轮非平衡 Feistel 结构

本文件演示两种常用工作模式：
- ECB：每个分组独立加密，相同明文块产生相同密文块，会泄露数据模式，不要用于真实业务。
- CBC：每个明文块先与前一个密文块异或再加密，需要 16 字节随机 IV，是常见的安全用法。

依赖：pip install gmssl
"""

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

# 16 字节密钥，取自 GB/T 32907 标准示例
KEY = bytes.fromhex("0123456789abcdeffedcba9876543210")
# 16 字节初始向量；真实场景必须每次随机生成，并与密文一起保存
IV = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

PLAINTEXT = "SM4 对称加密 demo：你好，国密！"


def ecb_encrypt(data: bytes) -> bytes:
    cipher = CryptSM4()
    cipher.set_key(KEY, SM4_ENCRYPT)
    return cipher.crypt_ecb(data)


def ecb_decrypt(data: bytes) -> bytes:
    cipher = CryptSM4()
    cipher.set_key(KEY, SM4_DECRYPT)
    return cipher.crypt_ecb(data)


def cbc_encrypt(data: bytes, iv: bytes = IV) -> bytes:
    cipher = CryptSM4()
    cipher.set_key(KEY, SM4_ENCRYPT)
    return cipher.crypt_cbc(iv, data)


def cbc_decrypt(data: bytes, iv: bytes = IV) -> bytes:
    cipher = CryptSM4()
    cipher.set_key(KEY, SM4_DECRYPT)
    return cipher.crypt_cbc(iv, data)


def dump(label: str, value: bytes) -> None:
    """按十六进制打印，长度非 16 的整数倍说明 padding 生效了。"""
    print(f"{label:<24}{value.hex()}")
    print(f"{'  len':<24}{len(value)} bytes")


def demo_ecb() -> None:
    print("=" * 72)
    print("ECB 模式")
    print("=" * 72)
    raw = PLAINTEXT.encode("utf-8")
    ct = ecb_encrypt(raw)
    dump("plaintext (utf-8)", raw)
    dump("ciphertext (hex)", ct)
    dump("decrypted", ecb_decrypt(ct))
    assert ecb_decrypt(ct) == raw

    # ECB 的缺陷：同样的明文分组 -> 同样的密文分组
    same = b"A" * 16 + b"A" * 16
    same_ct = ecb_encrypt(same)
    print("\n相同明文分组两次加密后的密文：")
    print("  block1:", same_ct[:16].hex())
    print("  block2:", same_ct[16:32].hex())
    print("  -> 完全相同，ECB 会暴露明文结构")


def demo_cbc() -> None:
    print("\n" + "=" * 72)
    print("CBC 模式")
    print("=" * 72)
    raw = PLAINTEXT.encode("utf-8")
    ct = cbc_encrypt(raw)
    dump("plaintext (utf-8)", raw)
    dump("ciphertext (hex)", ct)
    dump("decrypted", cbc_decrypt(ct))
    assert cbc_decrypt(ct) == raw
    print("明文:", cbc_decrypt(ct).decode("utf-8"))

    # 同样明文、不同 IV -> 完全不同密文，这是 CBC 相比 ECB 的关键优势
    other_iv = bytes.fromhex("0f0e0d0c0b0a09080706050403020100")
    ct2 = cbc_encrypt(raw, other_iv)
    print("\n换一个 IV 后的密文:", ct2.hex())
    print("与原密文是否相同:", ct == ct2)


def demo_roundtrip_cases() -> None:
    print("\n" + "=" * 72)
    print("边界用例：正好 16 字节 / 空串 / 长数据")
    print("=" * 72)
    for text in ["0123456789abcdef", "", "x" * 1000]:
        ct = cbc_encrypt(text.encode())
        assert cbc_decrypt(ct) == text.encode(), text
        print(f"  in={len(text):>4} chars  ct={len(ct):>4} bytes  roundtrip=OK")


if __name__ == "__main__":
    demo_ecb()
    demo_cbc()
    demo_roundtrip_cases()
    print("\n全部断言通过。")
