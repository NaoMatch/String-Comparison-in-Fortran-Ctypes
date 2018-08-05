! COMPILE COMMAND
! gfortran -O3 -fbounds-check -shared  -g -o Damerau_Levenstein.dll Damerau_Levenstein.f90
! gfortran -O2 -fbounds-check -shared  -g -o Damerau_Levenstein.dll Damerau_Levenstein.f90

subroutine dameraulevenshteindistance(distance, char1, char2)
    implicit none
    integer(kind=8)  :: distance
    character(len=*) :: char1, char2
    integer(kind=8), allocatable :: dptable(:, :)
    integer(kind=8)  :: n, m, i, j, cost, vals(4), flag

    n = len_trim(char1)
    m = len_trim(char2)

    allocate(dptable(n+1, m+1)); dptable=0

    do i=1, n+1
        dptable(i,1) = i-1
    end do

    do j=1, m+1
        dptable(1, j) = j-1
    end do

    do j=2, m+1
        do i=2, n+1
            vals=0
            flag=0
            cost=0

            if (char1(i-1:i-1) .ne. char2(j-1:j-1)) cost=1
            vals(1) = dptable(i-1, j)   + 1
            vals(2) = dptable(i,   j-1) + 1
            vals(3) = dptable(i-1, j-1) + cost
            dptable(i, j) = minval(vals(1:3))

            if ( i .gt. 2 .and. j .gt. 2) then
                if (char1(i-1:i-1) .eq. char2(j-2:j-2) .and. char1(i-2:i-2) .eq. char2(j-1:j-1)) then
                    vals(4) = dptable(i-2, j-2) + cost
                    dptable(i, j) = minval((/dptable(i, j), vals(4)/))
                end if
            end if
        end do
    end do
    distance = dptable(n+1, m+1)
    deallocate(dptable)
end subroutine dameraulevenshteindistance

!
