## [📗 이것이 취업을 위한 코딩 테스트다 with 파이썬](https://github.com/ndb796/python-for-coding-test)     
---

### 3️⃣ Chapter 3 - Greedy
```
> 현재 상황에서 지금 당장 좋은 것만 선택하는 알고리즘  
> 기준에 따라 좋은 것을 선택하는 문제  
> 문제에서 '가장 큰 순서대로', '가장 작은 순서대로' 라는 기준을 말해줄 때가 많다.
```
- 거스름돈 문제 : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch3_Greedy/ch3_1_change.py)     
- **동빈이의 큰 수의 법칙** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch3_Greedy/ch3_2_ndb.py)       
- **숫자 카드게임** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch3_Greedy/ch3_2_card.py)  
### 4️⃣ Chapter 4 - Implementation
```
> 구현 : 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정  
> 구현 문제 : 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제  
```
* 상하좌우 :  [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/ex_4_1_updown.py) / [예제코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/ex_4_1_updown_sample.py)
* 시각 :  [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/ex_4_2_view.py)     
* **왕실의 나이트** :  [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/kingdom_knight.py) / [예제코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/kingdom_knight_sample.py)    
* **게임 개발** :  [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/game.py) / [예제코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch4_Implementation/game_sample.py)
### 5️⃣ Chapter 5 - DFS/BFS
```  
  # 스택 자료구조  
   -> 선입후출 ( 입구와 출구가 동일한 형태 ex.프링글스 과자 통 )  
   -> 자바에서  
       - Stack<Integer> s = new Stack<>();  
       - 삽입 : push  
       - 삭제 : pop  
```       
```       
  # 큐 자료구조  
   -> 선입선출 ( 입구와 출구가 모두 뚫려있는 형태 ex.터널, 대기표 )  
   -> 자바에서 
       - Queue<Integer> s = new LinkedList<>();  
       - 삽입 : offer  
       - 추출(삭제)&출력 : poll  
```       
```      
  # 재귀 함수(Recursive Function)  
   -> 자기 자신을 호출하는 함수  
   -> 재귀 함수의 종료 조건을 반드시 명시해야 한다.  
   -> 예 : 팩토리얼 문제, 유클리드 호제법(최대공약수 계산) 문제  
```   
```   
  # DFS ( 깊이 우선 탐색 )  
   -> 깊은 부분을 우선적으로 탐색하는 알고리즘  
   -> 스택 자료구조(or 재귀함수)를 이용 
     1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.  
     2. 스택의 최상단 노드(제일 최근에 들어온 노드)에 방문하지 않은 인접 노드가 하나라도 있으면, 
        그 노드를 스택에 넣고 방문 처리를 한다.  
        방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다(스택에서 삭제).  
     3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.   
```  
``` 
  # BFS ( 너비 우선 탐색 )  
   -> 가까운 노드부터 탐색하는 알고리즘  
   -> 큐 자료구조 이용  
     1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.  
     2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 
        모두 큐에 삽입하고 방문 처리를 한다.  
     3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.  
```  
 - DFS 기본 구현 : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/dfs.py)   
 - BFS 기본 구현 : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/bfs.py)  
 - **음료수 얼려 먹기** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/drink_sample.py) / [예제코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/drink_sample.py)
 - **미로탈출** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/maze_sample.py) / [예제코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch5_DFS%3ABFS/maze_sample.py)  
### 8️⃣ Chapter 8 - DP
 -> 아 나는 다이나믹 프로그래밍이 정말 너무너무너무 어렵다. 제일 어렵다.
```
     # 메모리를 적절히 사용하여 수행 시간을 효율성을 비약적으로 향상시키는 방법  
     # 이미 계산된 결과(작은 문제)는 별도의 메모리에 저장 -> 다시 계산 안하게  
     # 일반적으로 탑다운, 보텀업 으로 구성  
     # 이때 '다이나믹'은 자료구조의 '다이나믹'과 의미가 다름 (자료구조 : 실행 도중 공간 할당 / 알고리즘 : 별 의미 없음)
```
```
     # 조건  
       1. 최적 부분 구조 (Optimal Substructure)  
         : 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제 해결 가능  
       2. 중복되는 부분 문제(Overlapping Subproblem)  
         : 동일한 작은 문제를 반복적으로 해결할 때
```
```
     # 대표적인 다이나믹 프로그래밍 문제 : 피보나치 수열  
       -> 일반적인 재귀함수로 구현할 때, 한 번 계산했던 값을 계속 계산해야 하는 경우가 생길 수도 있어서 시간이 오래걸린다.  
       -> 메모제이션 기법을 사용해서 해결할 수 있다.  
          : 메모제이션 구현 - 한 번 구한 정보를 리스트에 저장.
```
```
     # Bottom-up 방식 (주로 사용)  
       -> 결과 저장용 리스트 : DP 테이블
```
```
     # Top-down 방식  
       -> 이전에 계산된 결과를 일시적으로 기록해 놓는 개념인 '메모제이션' 사용
```
```
     # 다이나믹 프로그래밍 문제에 접근하는 방법  
       -> 먼저 그리디. 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는 지 검토
```
 - **개미전사** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch8_DP/dp_ant.py) / [예제코드](https://github.com/ndb796/python-for-coding-test/blob/master/8/6.py)
 - **바닥공사** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch8_DP/dp_floor.py) / [예제코드](https://github.com/ndb796/python-for-coding-test/blob/master/8/7.py)
 - **효율적인 화페구성** : [Python 코드](https://github.com/yougi8/CodingTestStudy/blob/main/%EC%9D%B4%EC%BD%94%ED%85%8C/ch8_DP/dp_coin.py) / [예제코드](https://github.com/ndb796/python-for-coding-test/blob/master/8/8.py)
