public class BinarySearch {
    int colLength ;
    int [][]matrix ;
    public Boolean search2DMatrix(int[][]matrix,int target){
        this.matrix = matrix ;
        colLength = matrix[0].length;
        int matrixLen = colLength * matrix.length;
        return search(0,matrixLen-1,target);
    }

    public Boolean search (int left,int right,int target){
        int mid = left +(right-left)/2;
        if(left<=right){
            int row = mid/colLength ;
            int col = mid%colLength ;
            if(this.matrix[row][col] == target){
                return true ;
            } else if (this.matrix[row][col] > target) {
                return search(left,mid-1,target);
            }else {
                return search(mid+1,right,target);
            }
        }
        return false;
    }

}
