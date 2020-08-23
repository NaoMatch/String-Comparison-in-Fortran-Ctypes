subroutine gestaltpatternmatching(gpmscore, string1, string2)
    implicit none
    character(len=*) :: string1, string2
    integer(kind=8) :: gpmscore
    ! To reserve consistency 'difflib'.
    ! gpmscore = 2.0*LCSubstrScore(string2, string1)/(len_trim(string1) + len_trim(string2)+0.0)
    gpmscore = 2*LCSubstrScore(string2, string1)
contains
    recursive integer function LCSubstrScore(char1, char2) result(res)
        ! Position Setting MUST be refered from the original Characters' one.
        implicit none
        character(len=*), intent(in) :: char1, char2
        integer :: char1_ini, char1_fin, char2_ini, char2_fin
        integer :: scores(3), lcsscore, dummy(2)

        ! c1f_ini = Character 1 Front Part Initial Position
        integer :: c1f_ini, c1f_fin, c2f_ini, c2f_fin, c1r_ini, c1r_fin, c2r_ini, c2r_fin

        char1_ini=1; char1_fin=len_trim(char1)
        char2_ini=1; char2_fin=len_trim(char2)

        ! Calculate LCSubstring Length & Their Rear Position
        scores = LCSubstrLenPosi(char1, char2)

        ! Front Part
        c1f_ini = char1_ini; c1f_fin = scores(2)-scores(1)
        c2f_ini = char2_ini; c2f_fin = scores(3)-scores(1)

        ! Rear Part
        c1r_ini = scores(2)+1; c1r_fin = char1_fin
        c2r_ini = scores(3)+1; c2r_fin = char2_fin
        res = scores(1)
        if ( c1f_fin - c1f_ini .ge. 0 .and. c2f_fin - c2f_ini .ge. 0 .and. scores(1) .ne. 0) then
            dummy(1) = LCSubstrScore(char1(c1f_ini:c1f_fin), char2(c2f_ini:c2f_fin))
            res = dummy(1) + res
        end if

        if ( c1r_fin - c1r_ini .ge. 0 .and. c2r_fin - c2r_ini .ge. 0 .and. scores(1) .ne. 0) then
            dummy(2) = LCSubstrScore(char1(c1r_ini:c1r_fin), char2(c2r_ini:c2r_fin))
            res = dummy(2) + res
        end if
    end function LCSubstrScore

    function LCSubstrLenPosi(char1, char2)
        implicit none
        character(len=*), intent(in) :: char1, char2
        integer :: lcsTable(len_trim(char1), len_trim(char2))
        integer :: LCSubstrLenPosi(3), i, j, f
        integer :: len_char1, len_char2, val
        character(len=1) :: tmp

        len_char1 = len_trim(char1)
        len_char2 = len_trim(char2)
        lcsTable=0

        tmp = char2(1:1)
        do i=1, len_char1
            lcsTable(i, 1) = tmp .eq. char1(i:i)
        end do

        tmp = char1(1:1)
        do j=1, len_char2
            lcsTable(1, j) = tmp .eq. char2(j:j)
        end do

        do j=2, len_char2
            tmp = char2(j:j)
            do i=2, len_char1
                f = char1(i:i) .eq. tmp
                val = lcsTable(i-1, j-1)+1
                lcsTable(i, j) = minval((/val, val*f/))
            end do
        end do

        ! Results
        LCSubstrLenPosi(1)   = maxval(lcsTable)
        LCSubstrLenPosi(2:3) = maxloc(lcsTable)
    end function LCSubstrLenPosi
end subroutine gestaltpatternmatching
