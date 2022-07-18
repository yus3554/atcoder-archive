N = gets.to_f
ans = 0

if N % 2 == 1 then
  ans = ((N.to_i/2 + 1) / N)
else
  ans = ((N.to_i/2) / N)
end

p ans
