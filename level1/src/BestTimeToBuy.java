public class BestTimeToBuy {

    public int totalProfit(int[]prices){
        int min = prices[0];
        int maxProfit = 0;
        for(int price:prices){
            min = Math.min(min,price);
            int sub = price - min;
            maxProfit = Math.max(maxProfit,sub);
        }
        return maxProfit;
    }
}
