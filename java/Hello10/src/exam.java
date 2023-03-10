// class 는 자바의 기본 블록

public class exam {
	public static void main(String[] args) {
		//main 는 함수(메소드 method)는 프로그램의 시작
	    //프로그램의 진입점 enrty point
		// main은 모든 클래스 생성시 변경??????????????

		System.out.print(21); //자바 출력 기본
		System.out.println(1); //println은 줄 띄움
		System.out.println("aserhagg");
		
		//변수의 선언(이제부터 변수 ~를 쓸거야;
		//메모리에 공간이 생기고 이름이 붙여진다 <-> 파이썬하고 차이점)
		int x; // 정수형
		int y = 5; // 변수의 초기값 가능 
		double d; //실수형,  10은 정수형 상수 -10.0은 실수형 상수
		boolean b; //불리언(참/거짓)
		String s; //문자열
	    //대입문, 할당문

		x =10; //x에 10을 저장 ; 지금부터 x값은 10이야
		y =x; // 현재 x값을 y에 저장해라.
		d =10.0;
		x = 1+2;
		x = y+1;
		x = x+1;
		b = false;
		s = "홍길동";
		System.out.println(x);
		
		int z =0 ; 
		z=z+1;
		System.out.println(z);
		z=z+1;
		System.out.println(z);
		z=z+1;
		System.out.println(z);
		z=z+1;
		System.out.println(z);
		z=z+1;
		System.out.println(z);
	}

}
