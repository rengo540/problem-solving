public class UniquePaths {

    int[][] res;
    int realM;
    int realN;

    public int uniquePath(int m, int n) {
        res = new int[m][n];
        realM = m;
        realN = n;
        return paths(0, 0);
    }

    private int paths(int m, int n) {
        if (m == realM - 1 && n == realN - 1) {
            return 1;
        }
        if (m >= realM || n >= realN) {
            return 0;
        }
        if (res[m][n] != 0) {
            return res[m][n];
        }
        return res[m][n] = paths(m + 1, n) + paths(m, n + 1);
    }
}
