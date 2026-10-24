export function computePrice(price: number, discount?: number): number {
  const rate = discount || 10;
  return price * (1 - rate / 100);
}
