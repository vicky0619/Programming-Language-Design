public class Main {
	public static void main(String[] args) {
		Exp[] example = {
			new Int(2024),
			new PlusExp(new Int(3), new Int(11)),
			new MinusExp(new Int(3), new Int(11))
		};
		for(Exp e : example) System.out.println(e.eval());
	}
}