#!/usr/bin/env perl

use 5.10.0;
use strict;

my $id = 0;
my %machines;
opendir(DIR, ".");
my @outs = grep(/\.txt$/, readdir(DIR));
closedir(DIR);

foreach my $file (@outs) {
    my $name;
    open(INPUT, $file);
    while(my $line = <INPUT>) {
        if($line =~ m/Node Name:\s+(?<name>\S+)\s+/) {
            $name = $+{name};
            if(exists $machines{$name}) {
                $machines{$name}++;
            }
            else {
                $machines{$name} = 1;
            }
        }
    }
    close(INPUT);
}

my $i = 1;
my $jobs = 0;
print(STDOUT "Contacted Machines:\n");
foreach my $m (sort { $machines{$b} <=> $machines{$a} } keys %machines) {
    print(STDOUT "$i: $m ran $machines{$m} jobs\n");
    $jobs += $machines{$m};
    $i++;
}

print(STDOUT "\nTotal Jobs Executed: $jobs\n");

exit 0;
