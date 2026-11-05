
public class Term {
    int coefficient;
    int degree;

    public Term(int coefficient, int degree) {
        this.coefficient = coefficient;
        this.degree = degree;
    }

    @Override
    public String toString() {
        if (degree > 1) {
            return "" + coefficient;
        }
        return "" + coefficient + "x^" + degree;
    }
}