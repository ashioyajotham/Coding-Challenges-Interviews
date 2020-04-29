// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public String solution(int[] T) {
        // write your code in Java SE 8
        String[] seasons = {"WINTER", "SPRING", "SUMMER", "AUTUMN"};
        int season = T.length / 4;
        int currMin = 9999;
        int currMax = -9999;
        
        int index = -1;
        int i = 0;
        int maxAmp = -1;
        
        while (i < T.length) {
            if (T[i] < currMin) {
                currMin = T[i];
            }
            
            if (T[i] > currMax) {
                currMax = T[i];
            }
            
            
            i += 1;
            if (i % season == 0) {
                
                if (Math.abs(currMin - currMax) > maxAmp) {
                    maxAmp = Math.abs(currMin - currMax);
                    index = i / season - 1;
                }
                currMin = 9999;
                currMax = -9999;
            }
        }
        
        
        return seasons[index];
            
    }
}
