public class Bool extends Exp {
    private boolean value;

    public Bool(boolean value) {
        this.value = value;
    }

    public Boolean eval() {
        return this.value;
    }

    public String toSExp() {
        return this.value ? "T" : "F";
    }
}
