package com.test.ezjvav;

import org.springframework.beans.factory.xml.BeanDefinitionParserDelegate;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Base64;

public class SerTest {
    public String ser(String ser) throws IOException, ClassNotFoundException {
        ser="3";
        System.out.println(ser);
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(Base64.getDecoder().decode(ser.getBytes()));
        ObjectInputStream objectInputStream = new ObjectInputStream(byteArrayInputStream);
        boolean x = objectInputStream.readBoolean();
        if (x) {
            objectInputStream.readObject();
            return "index";
        }
        return "index";
    }

}
