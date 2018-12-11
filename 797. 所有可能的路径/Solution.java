class Solution {
    private List<List<Integer>> allPaths = new ArrayList<>();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int[][] graph_process = new int[graph.length][graph.length];

        // 创建邻接表存储信息
        for (int i = 0; i < graph.length; i++) {
            for (int node : graph[i]) {
                graph_process[i][node] = 1;
            }
        }

        // 最后一个节点是 n-1
        int target = graph.length - 1;
        List<Integer> temp = new ArrayList<>();
        // 进行回溯
        getPath(graph_process, temp, 0, target);
        return allPaths;
    }

    private void getPath(int[][] Adjtable, List<Integer> temp, int cur, int target) {
        if (cur == target) {
            List<Integer> temp2 = new ArrayList<>(temp);
            temp2.add(0, 0);
            allPaths.add(temp2);
            return;
        }

        for (int i = 0; i < Adjtable[cur].length; i++) {
            if (Adjtable[cur][i] == 1) {
                temp.add(i);
                getPath(Adjtable, temp, i, target);
                temp.remove(temp.size() - 1);
            }
        }

        return;
    }
}