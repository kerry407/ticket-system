import styles from './Card.module.css'
import Image from 'next/image'
import bg1 from '../../public/Images/tech.avif'
import owner from '../../public/Images/owner.png'

const Card = () => {
  return (
    <div>
      <div className={styles.img}>
        <Image src={bg1} objectFit='cover' layout="fill" alt='Hero-Image' />
      </div>
      <div className={styles.details}>
      <h2>Women in Tech Rising: Embracing Equity</h2>
      <h3>Sat, Mar 18, 10:00 AM</h3>
      <p>
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex id quas eum hic eos natus....
      <span>Technology</span>
      </p>
      <div className={styles.owner}>
        <div>CSO global records inc. </div>
        <div className={styles.ownerImg}>
        <Image src={owner} objectFit='cover' layout="fill" alt='Hero-Image' />
        </div>
      </div>
      </div>
      
    </div>
  )
}

export default Card