
public class TestJDKClassLoader {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(String.class.getClassLoader());
//		System.out.println(com.sun.crypto.provider.DESKeyFactory.class.getClassLoader().getClass().getName());
		System.out.println(TestJDKClassLoader.class.getClassLoader().getClass().getName());
		System.out.println(ClassLoader.getSystemClassLoader());
		
		System.out.println("�鿴�̳й�ϵ");
		ClassLoader c = TestJDKClassLoader.class.getClassLoader();
		while (c != null) {
			System.out.println(c.getClass().getName());
			c = c.getParent();
		}
	}
	

}
