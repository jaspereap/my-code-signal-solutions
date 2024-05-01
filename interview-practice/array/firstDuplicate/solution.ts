function solution(a: number[]): number {
    let track = new Set<number>();
    for (let num of a) {
      if (track.has(num)) {
        return num;
      }
      track.add(num);
    }
    return -1;
  }