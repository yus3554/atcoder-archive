N = gets.to_i

Ns = N.to_s

An = (Ns[0].to_i) * (10 ** (Ns.length - 1)) - 1

def aaa(n, a)
    if n < 1 then
        return a
    end
    a += n % 10
    return aaa(n / 10, a)
end

aaan = aaa(N, 0)
aaaa = aaa(An, 0)

if aaan < aaaa then
    puts aaaa
else
    puts aaan
end