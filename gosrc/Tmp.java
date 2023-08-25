/*

each point is represented by {x, y}, both x and y are float numbers
unit square: each side has length 1.
all edges are either horizontal or vertical.

input: n points
output: find maximum number of points that can be covered by a unit square.

example:
{0.1, 0.1}, {0.2, 0.3}, {100, 200}, {0.8, 0.9}
output should be 3


 */

import java.util.NavigableMap;
import java.util.TreeMap;
import java.util.TreeSet;

class Tmp {

    public int coveredPoints(Double[][] points) {
        if (points == null) return 0;
        TreeMap<Double, TreeMap<Double, Integer>> map = new TreeMap<>();
        for (Double[] point : points) {
            map.putIfAbsent(point[0], new TreeMap<>());
            map.get(point[0]).put(point[1], map.get(point[0]).getOrDefault(point[1], 0) + 1);
        }

        int maxCount = 0;
        for (Double key : map.keySet()) {
            maxCount = Math.max(maxCount, countFromXKey(key, map));
        }
        return maxCount;
    }

    int countFromXKey(Double xkey, TreeMap<Double, TreeMap<Double, Integer>> map) {
        Double upperKey = map.floorKey(xkey + 1);
        NavigableMap<Double, TreeMap<Double, Integer>> subMap = map.subMap(xkey, true, upperKey, true);
        Double minYKey = getMinYKey(subMap);

        int maxCount = 0;
        while (true) {
            Double[] countMinYKey = countFromYKey(minYKey, subMap);
            int count = countMinYKey[0].intValue();
            minYKey = countMinYKey[1];
            maxCount = Math.max(maxCount, count);
            if (minYKey == null) {
                break;
            }
        }
        return maxCount;
    }

    private Double[] countFromYKey(Double minYKey, NavigableMap<Double, TreeMap<Double, Integer>> subMap) {
        int count = 0;
        Double nextYKey = null;
        for (Double xkey : subMap.keySet()) {
            NavigableMap<Double, Integer> subYMap = subMap.get(xkey).subMap(minYKey, true, minYKey + 1, true);
            for (Double subKey : subYMap.keySet()) {
                count += subMap.get(xkey).get(subKey);
            }
            nextYKey = nextYKey == null ? subMap.get(xkey).higherKey(minYKey) :
                    Math.min(nextYKey, subMap.get(xkey).higherKey(minYKey));
        }
        return new Double[]{count * 1.0D, nextYKey};
    }

    private Double getMinYKey(NavigableMap<Double, TreeMap<Double, Integer>> subMap) {
        Double nextMinKey = null;
        for (Double key : subMap.keySet()) {
            nextMinKey = nextMinKey == null ? subMap.get(key).firstKey() : Math.min(nextMinKey, subMap.get(key).firstKey());
        }
        return nextMinKey;
    }

    public static String Foo(String param) {
        return param;
    }

    public static void main(String[] args) {

        Double[][] input = new Double[][]{{0.1, 0.1D}, {0.2D, 0.3D}, {100D, 200D}, {0.8, 0.9}};
        int result = new Tmp().coveredPoints(input);
        System.out.println("Result3=" + result);

        input = new Double[][]{{0.1, 0.1D}, {0.1, 0.1D}, {0.2D, 0.3D}, {100D, 200D}, {0.8, 0.9}};
        result = new Tmp().coveredPoints(input);
        System.out.println("Result4=" + result);

        input = null;
        result = new Tmp().coveredPoints(input);
        System.out.println("Result0=" + result);
    }

}