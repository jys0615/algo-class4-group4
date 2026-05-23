package Lv2;

import java.util.*;

public class P_92341 {
    StringTokenizer st;
    Map<String, Integer> inTimeMap = new HashMap<>();
    Map<String, Integer> totalTimeMap = new HashMap<>();

    public int[] solution(int[] fees, String[] records) {
        for (String record : records) {
            st = new StringTokenizer(record);
            String time = st.nextToken();
            String carNum = st.nextToken();
            String act = st.nextToken();

            String[] timeArr = time.split(":");
            int totalTime = Integer.parseInt(timeArr[0]) * 60
                    + Integer.parseInt(timeArr[1]);

            if (act.equals("IN")) {
                inTimeMap.put(carNum, totalTime);
            } else {
                totalTimeMap.put(carNum,
                        totalTimeMap.getOrDefault(carNum, 0)
                                + totalTime - inTimeMap.get(carNum));
                inTimeMap.remove(carNum);
            }
        }

        for (Map.Entry<String, Integer> entry : inTimeMap.entrySet()) {
            String carNum = entry.getKey();
            int inTime = entry.getValue();
            totalTimeMap.put(carNum,
                    totalTimeMap.getOrDefault(carNum, 0)
                            + (23 * 60 + 59) - inTime);
            // inTimeMap.remove(carNum); Map순회 중 → put이나 remove 등 구조 변경x
        }

        List<String> carNumList = new ArrayList<>(totalTimeMap.keySet());
        carNumList.sort(null);

        int[] answer = new int[carNumList.size()];
        for (int i = 0; i < answer.length; i++) {
            int totalTime = totalTimeMap.get(carNumList.get(i));
            answer[i] = calculate(totalTime, fees);
        }

        return answer;
    }

    public int calculate(int totalTime, int[] fees) {
        int baseTime = fees[0];
        int baseFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];
        int additionalFee =
                ((totalTime - baseTime) + (unitTime - 1)) / unitTime * unitFee;

        // totalTime - baseTime < 0일 경우 처리 필요
        return baseFee + Math.max(0, additionalFee);
    }
}
