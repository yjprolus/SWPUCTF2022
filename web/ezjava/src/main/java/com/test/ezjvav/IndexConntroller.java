package com.test.ezjvav;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.util.Base64;

import org.springframework.beans.factory.xml.BeanDefinitionParserDelegate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
/* loaded from: ezjvav.jar:BOOT-INF/classes/com/test/ezjvav/IndexConntroller.class */
public class IndexConntroller {
    @RequestMapping({"/test"})
    public String unser(@RequestParam(name = "ser", required = true) String ser, Model model) throws IOException, ClassNotFoundException {
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(Base64.getDecoder().decode(ser.getBytes()));
        TestObjectInputStream objectInputStream = new TestObjectInputStream(byteArrayInputStream);
        boolean x = objectInputStream.readBoolean();
        if (x) {
            objectInputStream.readObject();
            return BeanDefinitionParserDelegate.INDEX_ATTRIBUTE;
        }
        return BeanDefinitionParserDelegate.INDEX_ATTRIBUTE;
    }
}
