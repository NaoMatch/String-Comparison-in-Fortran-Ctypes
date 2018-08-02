! COMPILE COMMAND
! gfortran -O3 -fbounds-check -shared  -g -o Jaro_Winkler.dll Jaro_Winkler.f90
! gfortran -O2 -fbounds-check -shared  -g -o Jaro_Winkler.dll Jaro_Winkler.f90

subroutine jarodistance(distance, char1, char2)
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    real(kind=8), intent(out)  :: distance
    ! Privates:
    real(kind=8)     :: weight1, weight2, weightt, double
    integer(kind=8)  :: txtrange, i, j, k, len1, len2, ini, fin
    integer(kind=8)  :: match_cnt, dummy, trans_cnt
    character(len=1) :: tmp
    logical, allocatable :: match_idx1(:), match_idx2(:)
    ! Initialization
    k=1
    dummy=0
    match_cnt=0
    trans_cnt=0

    ! Weights
    weight1=0.333333333333333333333333333333333333333
    weight2=weight1
    weightt=weight1

    ! Length & Range
    len1=len_trim(char1)
    len2=len_trim(char2)
    txtrange=maxval((/len1, len2/)) / 2-1

    allocate(match_idx1(len1)); match_idx1=.false.
    allocate(match_idx2(len2)); match_idx2=.false.

    ! Comparison
    do i=1, len1
        tmp=char1(i:i)
        ini=maxval((/i-txtrange, 1+dummy/))
        fin=minval((/i+txtrange, len2/))
        do j=ini, fin
            if (match_idx2(j)) cycle
            if (char2(j:j) .ne. tmp) cycle
            match_idx1(i) = .true.
            match_idx2(j) = .true.
            match_cnt=match_cnt+1
            exit
        end do
    end do

    ! Calculate Hamming Distance
    do i=1, len1
        if (.not. match_idx1(i)) cycle      ! Character Mismatch, SKIP
        do j=k, len2
            if (match_idx2(j))  exit        ! Searching Matched Character of char2
        end do
        if (char1(i:i) .ne. char2(j:j)) then    ! Transposition Case
            trans_cnt=trans_cnt+1
        end if
        k=j+1                                   ! Next Loop Initial Index
    end do

    ! Calculate Jaro Distance
    double = dble(match_cnt)
    distance = weight1 * (                        &
    &   double / dble(len1) + double / dble(len2) &
    & + (match_cnt-dble(trans_cnt/2.0)) / double)
    distance=1.0-distance
end subroutine jarodistance

















!
