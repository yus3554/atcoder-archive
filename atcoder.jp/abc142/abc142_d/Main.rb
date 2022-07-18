require 'prime'

A, B = gets.split.map { |e| e.to_i }

# 最大公約数
def gcd(a, b)
  t = 0
  while b != 0 do
    t = a % b
    a = b
    b = t
  end
  return a
end

p Prime.prime_division(gcd(A, B)).length + 1
