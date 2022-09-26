package com.test.ezjvav;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/* loaded from: classes3.dex */
public class check {
    static char[] hex = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    public boolean checkSN(String userName, String sn) throws NoSuchAlgorithmException {
        MessageDigest md5 = MessageDigest.getInstance("MD5");
        md5.update(userName.getBytes());
        if (userName.equals("swpu") && byte2str(md5.digest()).toLowerCase().equals(sn)) {
            return true;
        }
        return false;
    }

    private static String byte2str(byte[] bytes) {
        StringBuffer result = new StringBuffer();
        for (byte byte0 : bytes) {
            result.append(hex[(byte0 >>> 4) & 15]);
            result.append(hex[byte0 & 15]);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String userName="swpu";
        System.out.println(byte2str(userName.getBytes()));
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            System.out.println(md);
            System.out.printf(byte2str(md.digest()).toLowerCase());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }
}