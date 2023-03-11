import Image from 'next/image'
import styles from './Hero.module.css'
import bg1 from '../../public/Images/bg-1.jpeg'

const Hero = () => {
  return (
    <div className={styles.Hero}>
      <Image src={bg1} layout="fill" alt='Hero-Image' />
      <div className={styles.overlay}></div>
      <div className={styles.banner}>
        <div>
          <div className={styles.date}>
            <div>23</div>
            <div>05</div>
            <div>MAY<br /></div> 
            <div>2023</div>
          </div>
        </div>
        <div>
          <h2>PRESENTING...</h2>
          <h1><span>#1</span> Virtual Video
            <br />Marketing <span>Conference.</span>
          </h1>
          <button>Get Tickets</button><button className={styles.learn}>Learn More</button> 
        </div>
      </div>
    </div>
  )
}

export default Hero