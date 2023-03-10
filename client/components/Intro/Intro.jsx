import Card from '../Card/Card'
import styles from './Intro.module.css'

const Intro = () => {
  return (
    <div className={styles.intro}>
        <h2>Popular Events in <span>Lagos</span></h2>
        <h3>Filter by Category</h3>

        <div className={styles.events}>
            {
                [...Array(3)].map((x,i) => (
                    <Card key={i} />
                ))
            }
        </div>
    </div>
  )
}

export default Intro