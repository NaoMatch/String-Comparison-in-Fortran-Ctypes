! COMPILE COMMAND
! gfortran -O3 -fbounds-check -shared  -g -o Levenstein.dll Levenstein.f90
! gfortran -O2 -fbounds-check -shared  -g -o Levenstein.dll Levenstein.f90

subroutine levenshteindistance(distance, char1, char2)
    implicit none
    integer(kind=8)  :: distance
    character(len=*) :: char1, char2
    integer(kind=8), allocatable :: dptable(:, :)
    integer(kind=8) :: n, m, i, j, cost, val1, val2, val3

    n = len_trim(char1)
    m = len_trim(char2)

    allocate(dptable(n+1, m+1)); dptable=0

    do i=1, n+1
        dptable(i, 1) = i-1
    end do

    do j=1, m+1
        dptable(1, j) = j-1
    end do

    do j=2, m+1
        do i=2, n+1
            cost=0
            if (char1(i-1:i-1) .ne. char2(j-1:j-1)) cost=1
            val1 = dptable(i-1, j) + 1
            val2 = dptable(i, j-1) + 1
            val3 = dptable(i-1, j-1) + cost
            dptable(i, j) = minval((/val1, val2, val3/))
        end do
    end do
    distance = dptable(n+1, m+1)
end subroutine levenshteindistance








































!
