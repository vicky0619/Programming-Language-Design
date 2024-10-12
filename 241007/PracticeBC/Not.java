public class Not extends Exp {
    private Exp e;

    public Not(Exp e) {
        this.e = e;
    }

    public Boolean eval() {
        return !(Boolean) e.eval();
    }

    public String toSExp() {
        return "[not " + e.toSExp() + "]";
    }
}
