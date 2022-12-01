#!/usr/bin/perl

use strict;
use warnings;

my $document = do {
    local $/ = undef;
    open my $fh, "<", "inputs/day1.txt" or die "$!";
    <$fh>;
};

my @elves = ();
foreach ( split(/\n\n/, $document) ) {
    my $sum = 0;
    map { $sum += $_ } split(/\n/);
    push @elves, $sum;
}

my @sorted = sort { $b <=> $a } @elves;
printf("Day 1, part 1: %d\n", $sorted[0]);
my $topthree = 0;
map { $topthree += $_ } @sorted[0..2];
printf("Day 1, part 2: %d\n", $topthree);
