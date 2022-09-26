package com.test.ezjvav;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Base64;
import org.springframework.beans.factory.xml.BeanDefinitionParserDelegate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
/* loaded from: ezjvav.jar:BOOT-INF/classes/com/test/ezjvav/UnserConntroller.class */
public class UnserConntroller {
    @RequestMapping({"/unser"})
    public String unser(@RequestParam(name = "ser", required = true) String ser, Model model) throws IOException, ClassNotFoundException {
        System.out.println(ser);
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(Base64.getDecoder().decode(ser.getBytes()));
        ObjectInputStream objectInputStream = new ObjectInputStream(byteArrayInputStream);
        boolean x = objectInputStream.readBoolean();
        if (x) {
            objectInputStream.readObject();
            return BeanDefinitionParserDelegate.INDEX_ATTRIBUTE;
        }
        return BeanDefinitionParserDelegate.INDEX_ATTRIBUTE;
    }
}
