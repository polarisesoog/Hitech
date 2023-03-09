
public class ex5 {

	public static void main(String[] args) {
		int x = 300;
		System.out.println(x);
		byte b = 127;
		b = (byte)x ;      // 집어 넣으려는 타입을 ()로 감싸서 강제 타입변경
		System.out.println(b);
		
		final double PI = 3.14;
		float r = 2.f;
		float a = (float)(PI * r * r);
		// 집어 넣으려는 타입을 ()로 감싸서 강제 타입변경
		System.out.println(a);
		int j = (int)a;
		System.out.println(j);
		
		System.out.println(a-j);


	}

}
