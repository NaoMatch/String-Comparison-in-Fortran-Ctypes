! COMPILE COMMAND
! gfortran -O3 -shared  -g -o LCSubSeq.dll LCSubSeq.f90
! gfortran -O2 -shared  -g -o LCSubSeq.dll LCSubSeq.f90

subroutine lcsubseq_len(length, char1, char2)
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    integer(kind=8)  :: length
    ! Privates:
    integer(kind=8)  :: dptable(len_trim(char1)+1, len_trim(char2)+1), i, j
    dptable=0

    do j=2, len_trim(char2)+1
        do i=2, len_trim(char1)+1
            if (char1(i-1:i-1) .eq. char2(j-1:j-1)) then
                dptable(i, j) = dptable(i-1, j-1) + 1
            else
                dptable(i, j) = maxval((/dptable(i, j-1), dptable(i-1, j)/))
            end if
        end do
    end do

    length = maxval(dptable)

end subroutine lcsubseq_len

subroutine lcsubseq_pos(position, char1, char2)
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    integer(kind=8) :: position(minval((/len_trim(char1), len_trim(char2)/)))
    ! Privates:
    integer(kind=8)  :: dptable(len_trim(char1)+1, len_trim(char2)+1), i, j, fill
    dptable=0
    position=0
    do j=2, len_trim(char2)+1
        do i=2, len_trim(char1)+1
            if (char1(i-1:i-1) .eq. char2(j-1:j-1)) then
                dptable(i, j) = dptable(i-1, j-1) + 1
            else
                dptable(i, j) = maxval((/dptable(i, j-1), dptable(i-1, j)/))
            end if
        end do
    end do

    i = len_trim(char1)+1
    j = len_trim(char2)+1

    fill=1
    do while (i .ne. 1 .and. j .ne. 1)
        if      (dptable(i, j) .eq. dptable(i-1, j)) then
            i = i-1
        else if (dptable(i, j) .eq. dptable(i, j-1)) then
            j = j-1
        else
            position(fill) = i-1
            fill=fill+1
            i = i-1
            j = j-1
        end if
    end do

end subroutine lcsubseq_pos
