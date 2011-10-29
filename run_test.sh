#!/bin/bash


# Copyright (c) Brody Holden, 2011
# Runs all files matching "test_*.py".
# Requires python (tested for 2.7.x) and pep8.


PEP8_SHARED_FLAGS=" --verbose --repeat --ignore=E241 "
PEP8_FULL="pep8 --show-source --show-pep8 "
PEP8="pep8 --show-source "
PEP8_MIN="pep8 "
OPT_DO_PEP8=false


function usage
{
    echo "Usage: $0 <options>"
    echo
    echo "Options:"
    echo "  -h or --help        Diplay this help menu."
    echo "  -c or --clear       Clear terminal twice before running tests."
    echo "  --pep8              pep8 with extra --show-source"
    echo "  --pep8-full         pep8 with extra --show-source --show-pep8"
    echo "  --pep8-min          pep8 with no extras."
    echo
    echo "The pep8 options above run pep8 on all *.py to validate them to the"
    echo "pep8 style guide. All pep8 include: --verbose --repeat --ignore=E241"
    echo "pep8 must be install for --pep8* options to work."
    echo
    echo "When using two or more parameters that start with a single '-', "
    echo "don't combine them into one. Example:"
    echo "  $0 -h -c            <- Right"
    echo "  $0 -hc              <- Wrong"
}


function pep8_tests
{
    local py_files=$(ls *.py)

    echo
    echo "PEP8 style guide:"

    for py in $py_files
    do
        $PEP8 $PEP8_SHARED_FLAGS $py
    done
}


# Collect passed parameters
for p in "$@"
do
    case "$p" in
    "-h" | "--help")
        usage
        exit
        ;;
    "-c" | "--clear-first")
        clear
        clear
        ;;
    "--pep8")
        OPT_DO_PEP8=true
        ;;
    "--pep8-full")
        echo "FULL"
        OPT_DO_PEP8=true
        PEP8=$PEP8_FULL
        ;;
    "--pep8-min")
        echo "MIN"
        OPT_DO_PEP8=true
        PEP8=$PEP8_MIN
        ;;
    esac
done


# Python Unittesting
echo "Python Unittesting:"

TEST_LIST=$(ls test_*.py)

for TEST_SCRIPT in $TEST_LIST
do
    echo $TEST_SCRIPT
    python $TEST_SCRIPT
done

# PEP8 - Style Guide
if [ $OPT_DO_PEP8 == true ]
then
    pep8_tests
fi
