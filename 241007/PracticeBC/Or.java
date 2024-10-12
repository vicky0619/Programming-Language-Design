public class Or extends Exp {
    private Exp e1, e2;

    public Or(Exp e1, Exp e2) {
        this.e1 = e1;
        this.e2 = e2;
    }

    public Boolean eval() {
        return (Boolean) e1.eval() || (Boolean) e2.eval();
    }

    public String toSExp() {
        return "[or " + e1.toSExp() + " " + e2.toSExp() + "]";
    }
}
