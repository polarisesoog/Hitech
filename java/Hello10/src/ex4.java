
public class ex4 {

	public static void main(String[] args) {
		final float PI = 3.14f; 
		// final 타입 대문자이름 - 상수 선언 변경 불가 
		//상수의 이름은 전부 대문자
		// static final double PI = 3.14; //절대불변 우위 상수

		float r = 10.2f;  
		//자바에서는 double기본값 > float 개념(끝 f자 추가)
		float MyunJuk = PI * r * r;
		System.out.println("원의 면적은 " + MyunJuk);

		float DuLe = 2.0f * PI * r;
		System.out.println("원의 둘레는 " + DuLe);

	}

}
