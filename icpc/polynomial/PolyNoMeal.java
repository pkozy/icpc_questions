import java.util.ArrayList;

public class PolyNoMeal {
    public ArrayList<Term> terms;
    public int degree;

    public PolyNoMeal(int deg) {
        degree = deg;
        terms = new ArrayList<Term>();
    }

    public PolyNoMeal(ArrayList<Term> terms, int deg) {
        degree = deg;
        this.terms = terms;
    }

    public boolean addTerm(int coef, int deg) {
        terms.add(new Term(coef, deg));
        return true;
    }

    @Override
    public String toString() {
        String str = "";
        int i;
        for (i = 0; i <= degree-2; i++) {
            str += terms.get(i) + "+";
        }
        str += terms.get(i);
        return str;
    }
}