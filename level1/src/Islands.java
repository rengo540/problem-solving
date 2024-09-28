public class Islands {



    public int numberOfIslans(int [][] grid){

        int islandsCount =0;
        for(int i=0; i< grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] == 1){
                    dfs(i,j,grid);
                    islandsCount++;
                }
            }
        }
        return islandsCount;
    }


    public int maxAreaOIslans(int [][] grid){

        int maxArea =0;
        for(int i=0; i< grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j] == 1){
                    maxArea=Math.max(dfs(i,j,grid),maxArea);
                }
            }
        }
        return maxArea;
    }

    private int  dfs(int row,int col,int [][]grid){
        if(row >= grid.length || row <0){
            return 0;
        }
        if(col >= grid[0].length || col<0){
            return 0;
        }
        if(grid[row][col]==0){
            return 0;
        }
        int count =1 ;
        grid[row][col]=0;
        count +=dfs(row+1,col,grid);
        count +=dfs(row,col+1,grid);
        count +=dfs(row-1,col,grid);
        count +=dfs(row,col-1,grid);

        return count;
    }
}
