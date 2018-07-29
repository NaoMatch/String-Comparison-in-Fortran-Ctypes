! COMPILE COMMAND
! gfortran -O3 -shared  -g -o LCSubStr.dll LCSubStr.f90
! gfortran -O2 -shared  -g -o LCSubStr.dll LCSubStr.f90
subroutine lcsubstr_len(length, char1, char2)
    implicit none
    character(len=*), intent(in) :: char1, char2
    integer(kind=8) :: lcsTable(len_trim(char1), len_trim(char2))
    integer(kind=8) :: length, i, j

    lcsTable=0                                  ! Initialize
    do i=1, len_trim(char1)                     ! The 1st Character Matching
        if (char2(1:1) .eq. char1(i:i)) lcsTable(i, 1)=1
    end do

    do j=1, len_trim(char2)                     ! The 1st Character Matching
        if (char1(1:1) .eq. char2(j:j)) lcsTable(1, j)=1
    end do

    do j=2, len_trim(char2)
        do i=2, len_trim(char1)
            if (char1(i:i) .eq. char2(j:j)) lcsTable(i, j)=lcsTable(i-1, j-1)+1
        end do
    end do

    ! Results
    length = maxval(lcsTable)
end subroutine lcsubstr_len

subroutine lcsubstr_pos(position, char1, char2)
    implicit none
    character(len=*), intent(in) :: char1, char2
    integer(kind=8) :: lcsTable(len_trim(char1), len_trim(char2))
    integer(kind=8) :: position(3), i, j

    lcsTable=0                                  ! Initialize
    do i=1, len_trim(char1)                     ! The 1st Character Matching
        if (char2(1:1) .eq. char1(i:i)) lcsTable(i, 1)=1
    end do

    do j=1, len_trim(char2)                     ! The 1st Character Matching
        if (char1(1:1) .eq. char2(j:j)) lcsTable(1, j)=1
    end do

    do j=2, len_trim(char2)
        do i=2, len_trim(char1)
            if (char1(i:i) .eq. char2(j:j)) lcsTable(i, j)=lcsTable(i-1, j-1)+1
        end do
    end do

    ! Results
    position(1) = maxval(lcsTable)
    position(2:3) = maxloc(lcsTable)
end subroutine lcsubstr_pos
