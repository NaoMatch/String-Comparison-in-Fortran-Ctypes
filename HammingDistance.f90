! COMPILE COMMAND
! gfortran -O3 -fbounds-check -shared  -g -o HammingDistance.dll HammingDistance.f90
! gfortran -O2 -fbounds-check -shared  -g -o HammingDistance.dll HammingDistance.f90

subroutine hammingdistance(distance, char1, char2)
    ! Calculate Hamming Distance
    ! Args:
    !   char1: Input Character 1
    !   char2: Input Character 2
    ! Return:
    !   distance: hamming distance
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    integer(kind=8)  :: distance
    ! Privates:
    integer(kind=8)  :: i, length

    distance = 0                ! Initialize distance
    length = len_trim(char1)    ! Get Sting Length
    do i=1, length
        ! If two characters at position i are NOT equal
        if (char1(i:i) .ne. char2(i:i)) distance = distance + 1
    end do
end subroutine hammingdistance

subroutine hammingsimilarity(similarity, char1, char2)
    ! Calculate Hamming Similarity
    ! Args:
    !   char1: Input Character 1
    !   char2: Input Character 2
    ! Return:
    !   distance: hamming similarity (length of character - hamming distance)
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    integer(kind=8)  :: similarity
    ! Privates:
    integer(kind=8)  :: distance, i, length
    distance = 0
    length   = len_trim(char1)

    do i=1, length
        if (char1(i:i) .ne. char2(i:i)) distance = distance + 1
    end do
    similarity = length - distance
end subroutine hammingsimilarity

subroutine hammingdistance_norm(distance, char1, char2)
    ! Calculate Normalized Hamming Distance
    ! Args:
    !   char1: Input Character 1
    !   char2: Input Character 2
    ! Return:
    !   distance: normalized hamming distance
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    real(kind=8)  :: distance
    ! Privates:
    integer(kind=8)  :: i, length, dummy

    dummy = 0
    length = len_trim(char1)

    do i=1, length
        if (char1(i:i) .ne. char2(i:i)) dummy = dummy + 1
    end do
    distance = dble(dummy) / dble(length)
end subroutine hammingdistance_norm

subroutine hammingsimilarity_norm(similarity, char1, char2)
    ! Calculate Normalized Hamming Similarity
    ! Args:
    !   char1: Input Character 1
    !   char2: Input Character 2
    ! Return:
    !   distance: normalized hamming similarity (1 - normalized hamming distance)
    implicit none
    ! Args:
    character(len=*) :: char1, char2
    ! Return:
    real(kind=8)     :: similarity
    ! Privates
    integer(kind=8)  :: distance, dummy, i, length
    distance = 0
    length = len_trim(char1)

    do i=1, length
        if (char1(i:i) .ne. char2(i:i)) distance = distance + 1
    end do
    dummy = length - distance
    similarity = dummy / dble(length)
end subroutine hammingsimilarity_norm
