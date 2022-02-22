
sub g_print {
    print "$x\n";
}

sub test_my {
    my $x = 11;
    print "call-my $x\n";
    g_print;
}

sub test_local {
    local $x = 20;
    print "call-local $x\n";
    g_print;
}

$x = 9;
test_my;
test_local;
print "$x\n";
