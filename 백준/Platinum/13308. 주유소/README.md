# [Platinum V] 주유소 - 13308 

[문제 링크](https://www.acmicpc.net/problem/13308) 

### 성능 요약

메모리: 252972 KB, 시간: 5444 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 최단 경로, 데이크스트라

### 제출 일자

2025년 7월 6일 17:08:03

### 문제 설명

<p>어떤 나라에는 N개의 도시가 있고, 각 도시는 1번부터 N번까지 번호가 붙어 있다. 또, 서로 다른 두 도시를 양방향으로 직접 연결하는 M개의 도로가 있다. 도로들은 서로 길이가 다를 수 있다. 도로 길이의 단위는 km를 사용한다.</p>

<p>1번 도시에서 N번 도시로 자동차를 이용하여 이동하려고 한다. 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다. 기름통의 크기는 무제한이어서 얼마든지 많은 기름을 넣을 수 있다. 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다. 각 도시에는 단 하나의 주유소가 있으며, 도시마다 주유소의 리터당 가격은 다를 수 있다. 가격의 단위는 원을 사용한다.</p>

<p>예를 들어, 이 나라에 다음 그림처럼 4개의 도시와 4개의 도로가 있다고 하자. 원 안에 있는 숫자는 도시의 번호, 원 옆에 있는 숫자는 그 도시에 있는 주유소의 리터당 가격이다. 도로 옆에 있는 숫자는 도로의 길이를 표시한 것이다. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/13308/1.png" style="height:169px; width:224px"></p>

<p>1번 도시에서 출발할 때 7리터의 기름을 넣고 그 기름으로 4번 도시까지 (3번 도시를 거쳐) 이동하면 총 비용은 35원이다. 만약 1번 도시에서 출발할 때 3리터의 기름을 넣고(3×5 = 15원) 3번 도시로 이동한 다음, 다시 3번 도시에서 4리터의 기름을 넣고(4×4 = 16원) 4번 도시에 도착하면 총 비용은 31원이다. 또 다른 방법으로 1번 도시에서 2리터의 기름을 넣고(2×5 = 10원) 2번 도시로 이동하여, 2번 도시에서 9리터의 기름을 넣고(9×2 = 18원) 1번과 3번 도시를 거쳐 4번 도시에 도착하면 총 비용은 28원이다.</p>

<p>각 도시에 있는 주유소의 기름 가격과, 각 도로들의 길이를 입력으로 받아 1번 도시에서 N번 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.</p>

### 입력 

 <p>표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 도시의 수와 도로의 수를 나타내는 정수 N(2 ≤ N ≤ 2,500)과 정수 M(1 ≤ M ≤ 4,000)이 주어진다. 다음 줄에 각 도시 주유소의 리터당 가격이 도시 번호 순서대로 N개의 자연수로 주어진다. 리터당 가격은 1 이상 2,500 이하의 자연수이다. 그 다음 M개의 줄 각각에 하나의 도로에 대한 정보가 세 개의 자연수로 주어지는데, 처음 두 개의 자연수는 도로가 연결하는 두 도시의 번호이며, 세 번째 자연수는 도로의 길이이다. 도로의 길이는 1 이상 2,500 이하의 자연수이다. 한 쌍의 도시를 연결하는 도로는 최대 하나만 존재한다. 임의의 도시에서 다른 임의의 도시로 도로들을 이용하여 이동할 수 있는 방법이 항상 존재한다. </p>

### 출력 

 <p>표준 출력으로 1번 도시에서 N번 도시로 가는 최소 비용을 출력한다.</p>

