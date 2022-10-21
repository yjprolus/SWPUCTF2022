import org.apache.commons.codec.digest.DigestUtils;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Created by yjprolus on 2022/10/21.
 * SHA1测试类，加密工具包单独封装到一个工具类中，使用三种不同的方法生成
 */

public class SHA1Test {
    public static void main(String[] args) throws Exception {
        String message = "202031010347";
        System.out.println("消息明文：" + message);
        System.out.println("原生Java实现: " + SHA1Utils.generate1(message.getBytes()));
        System.out.println("Java内置类实现: " + SHA1Utils.generate2(message.getBytes()));
        System.out.println("cc方式实现实现: " + SHA1Utils.generate3(message));
    }
}

class SHA1Utils {
    // 第一种方法：根据教材算法实现
    public static String generate1(byte[] message1) throws Exception {

        byte[] fillBytes = new byte[64 * ((message1.length + 8) / 64 + 1)];
        int i;
        for (i = 0; i < message1.length; i++) {
            fillBytes[i] = message1[i];
        }

        // 填充 100000.....00
        fillBytes[i] = (byte) 0x80;

        // 填充长度
        long len = message1.length * 8L;
        for (int j = fillBytes.length - 8, k = 0; j < fillBytes.length; j++, k++) {
            fillBytes[j] = (byte) (len >> ((7 - k) * 8));
        }

        // 转换byte为int
        int[] bytes2Ints = byteArrToIntegerArr(fillBytes);
        int[] k = {0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6};
        int[] h = {0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0};

        for (int j = 0; j < bytes2Ints.length; j += 16) {
            int[] w = new int[80];
            System.arraycopy(bytes2Ints, 0, w, 0, 16);

            int a = h[0], b = h[1], c = h[2], d = h[3], e = h[4];

            for (int t = 0; t < 80; t++) {
                if (t >= 16) {
                    w[t] = loopLeftMove(1, w[t - 16] ^ w[t - 14] ^ w[t - 8] ^ w[t - 3]);
                }
                int temp = loopLeftMove(5, a) + f(t, b, c, d) + e + w[t] + k[t / 20];
                e = d;
                d = c;
                c = loopLeftMove(30, b);
                b = a;
                a = temp;
            }

            h[0] += a;
            h[1] += b;
            h[2] += c;
            h[3] += d;
            h[4] += e;
        }
        return String.format("%08x%08x%08x%08x%08x", h[0], h[1], h[2], h[3], h[4]);
    }

    // 第二种方法：JDK原生工具类 MessageDigest
    public static String generate2(byte[] message2) throws NoSuchAlgorithmException {
        MessageDigest messageDigest = MessageDigest.getInstance("SHA1");
        byte[] result = messageDigest.digest(message2);
        StringBuilder stringBuffer = new StringBuilder();
        for (byte b : result) {
            stringBuffer.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
        }
        return stringBuffer.toString();
    }

    // 第三种方法：Apache开源第三方工具包已有封装
    public static String generate3(String message3) {
        return DigestUtils.sha1Hex(message3);
    }

    // 计算分组的摘要值
    private static int f(int t, int b, int c, int d) {
        switch (t / 20) {
            case 0:
                return (b & c) | (~b & d);
            case 2:
                return (b & c) | (b & d) | (c & d);
            default:
                return b ^ c ^ d;
        }
    }

    // Java实现循环左移函数S的写法如下，注意>>>与>>的区别，两者均为右移，>>高位补符号位，>>>高位补0
    private static int loopLeftMove(int left_mov, int num) {
        return num << left_mov | num >>> (32 - left_mov);
    }

    private static int[] byteArrToIntegerArr(byte[] bytes) throws Exception {
        if (bytes.length % 4 != 0) {
            throw new Exception("格式化错误");
        }
        int[] intArr = new int[bytes.length / 4];
        for (int i = 0; i < intArr.length; i++) {
            intArr[i] = bytes[i * 4 + 3] & 0x000000ff |
                    bytes[i * 4 + 2] << 8 & 0x0000ff00 |
                    bytes[i * 4 + 1] << 16 & 0x00ff0000 |
                    bytes[i * 4] << 24 & 0xff000000;
        }
        return intArr;
    }
}
