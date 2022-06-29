import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class TestReflection {

	public static void main(String[] args) throws IllegalArgumentException, InvocationTargetException {
		// TODO Auto-generated method stub
		String str = "T";
		try {
			Class c = Class.forName(str);
			Object o = c.newInstance();
			Method[] methods = c.getMethods();
			for (Method m: methods) {
//				System.out.println(m.getName());
				if (m.getName().equals("mm")) {
					m.invoke(o);
				}
				if (m.getName().equals("m1")) {
					m.invoke(o, 1);
					for(Class paramType: m.getParameterTypes()) {
						System.out.println(paramType.getName());
					}
				}
				if (m.getName().equals("getS")) {
					Class returnType = m.getReturnType();
					System.out.println(returnType.getName());
				}
			}
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InstantiationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

class T{
	
	// 是否加载
	static {
		System.out.println("T loaded");
	}
	// 是否被创建实例
	public T() {
		System.out.println("T constructed ");
	}
	int i;
	String s;
	public void m1(int i) {
		this.i = i;
		System.out.println("m1 " + this.i);
	}
	public String getS() {
		return this.s;
	}
	
	public void mm() {
		System.out.println("mm invoked");
	}
}