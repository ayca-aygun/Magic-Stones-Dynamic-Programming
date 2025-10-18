from implement_hw import magic_stones_topdown, magic_stones_bottomup, count_flips

if __name__ == "__main__":
    # Test "magic stones" problem
    
    
    stones = [1, 45, 36, 47, 14, 21, 21, 40, 37, 44, 23, 3, 44, 11, 21, 20, 14, 29, 15, 33, 4, 29, 6, 11, 12, 44, 5, 37, 16, 6, 30, 39, 14, 27, 38, 47, 29, 47, 36, 25, 6, 15, 7, 30, 4, 36, 21, 46, 3, 15, 45, 4, 11, 43, 35, 8, 47, 5, 28, 48, 32, 41, 26, 23, 44, 13, 43, 44, 27, 29, 44, 45, 8, 7, 4, 15, 11, 44, 43, 10, 47, 44, 39, 21, 25, 34, 28, 47, 18, 20, 28, 13, 36, 35, 44, 37, 7, 2, 39, 40, 47]
    health = 970
    
    assert(magic_stones_topdown(stones, health) == 21)
    assert(magic_stones_bottomup(stones, health) == 21)
    
    stones = [1, 4, 6, 11, 25]
    health = 228
    assert(magic_stones_topdown(stones, health) == 11)
    assert(magic_stones_bottomup(stones, health) == 11)

    # Test "count flips" problem
    arr = [4, 1, 2, 1]
    assert(count_flips(arr) == 4)