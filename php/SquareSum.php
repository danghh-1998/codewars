<?php
/*
 * Complete the square sum function so that it squares each number passed into it and then sums the results together.
 *
 * For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
 *
 */

function square_sum($numbers): int
{
    return $numbers ? array_reduce(array_map(function ($item) {
        return $item * $item;
    }, $numbers), function ($sum, $item) {
        return $sum + $item;
    }) : 0;
}
