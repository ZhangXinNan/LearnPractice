
public class TestDynamicLoading {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new A();
		System.out.println("**---------------------------**");
		new B();
		new C();
		new C();
		new D();
		new D();
	}

}


class A {
	
}

class B {
	
}

class C {
	static {
		System.out.println("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCc");
	}
}

class D {
	{//¶¯Ì¬Óï¾ä¿é
		System.out.println("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD");
	}
}
