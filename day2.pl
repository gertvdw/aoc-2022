#!/usr/bin/perl

$game = do { local $/; open $fh, "<", "inputs/day2.txt" or die "$!"; <$fh>; };
$score = $matchfixed_score = 0;
%points = ("A", 1, "X", 1, "B", 2, "Y", 2, "C", 3, "Z", 3);
%losing_moves = ("A", "Z", "B", "X", "C", "Y");     # moves where I lose
%draw_moves = ("A", "X", "B", "Y", "C", "Z");       # moves that, you know, force a draw
%win_moves = ("A", "Y", "B", "Z", "C", "X");        # moves where I win
@winning_moves = ("XC", "YA", "ZB"); # leaving this in here, just for the "value" ~~ @winning_moves bit

map { 
    ($opp, $me) = split / /;
    $state = $matchfixed_state = "lost";
    $score += $points{$me};
    
    # part 2: honest game.
    if ($points{$opp} == $points{$me}) {
        $score += 3;
        $state = "draw";
    } elsif (sprintf("%s%s",$me,$opp) ~~ @winning_moves) {
        $score += 6;
        $state = "win";
    }

    # part 2: matchfixing.
    if ($me eq "X") {
        $matchfixed_score += $points{$losing_moves{$opp}};
    } elsif ($me eq "Y") {
        $matchfixed_score += 3 + $points{$draw_moves{$opp}};
        $matchfixed_state = "draw";
    } else {
        $matchfixed_score += 6 + $points{$win_moves{$opp}};
        $matchfixed_state = "win";
    }
    # printf("Opponent: %s, me: %s (%-4s) but matchfixing says (%-4s)\n", $opp, $me, $state, $matchfixed_state);
} split /\n/, $game;

printf("Day 2, part 1: %d\n", $score);
printf("Day 2, part 2: %d\n", $matchfixed_score);