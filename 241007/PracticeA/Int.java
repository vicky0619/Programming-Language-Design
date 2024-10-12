public class Int extends Exp {
	private int val;
	public Int(int val) {
	    this.val = val;
	}	
	public int eval() {
	    return this.val;
	}
	public String toSExp() {
        return String.valueOf(this.val);
    }
}
