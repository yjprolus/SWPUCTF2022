package com.test.ezjvav;

import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectStreamClass;
import java.util.ArrayList;
import java.util.Iterator;

/* loaded from: ezjvav.jar:BOOT-INF/classes/com/test/ezjvav/TestObjectInputStream.class */
public class TestObjectInputStream extends ObjectInputStream {
    public TestObjectInputStream(InputStream in) throws IOException {
        super(in);
    }

    @Override // java.io.ObjectInputStream
    protected Class<?> resolveClass(ObjectStreamClass osclass) throws IOException, ClassNotFoundException {
        ArrayList<String> blackList = new ArrayList<>();
        blackList.add("org.apache.commons.collections.Transformer");
        blackList.add("org.apache.commons.collections.functors.ConstantTransformer");
        blackList.add("org.apache.commons.collections.functors.ChainedTransformer");
        blackList.add("org.apache.commons.collections.functors.InvokerTransformer");
        blackList.add("org.apache.commons.collections.functors.InstantiateTransformer");
        blackList.add("javax.management.remote.rmi.RMIConnector");
        Iterator<String> it = blackList.iterator();
        while (it.hasNext()) {
            String s = it.next();
            if (osclass.getName().contains(s)) {
                throw new ClassNotFoundException("nonono,please Detour");
            }
        }
        return super.resolveClass(osclass);
    }
}
